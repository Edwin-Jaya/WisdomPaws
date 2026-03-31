import mediapipe as mp
import cv2
import time

BaseOptions = mp.tasks.BaseOptions
GestureRecognizer = mp.tasks.vision.GestureRecognizer
GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
GestureRecognizerResult = mp.tasks.vision.GestureRecognizerResult
VisionRunningMode = mp.tasks.vision.RunningMode


class Controller:
    def __init__(self, model_path="./Model/gesture_recognizer.task"):
        self.cam = cv2.VideoCapture(0)
        self.last_gesture = None   # current gesture
        self.prev_gesture = None   # previous gesture (to avoid spam)

        # Setup options
        options = GestureRecognizerOptions(
            base_options=BaseOptions(model_asset_path=model_path),
            running_mode=VisionRunningMode.LIVE_STREAM,
            result_callback=self._result_callback,
            num_hands=2
        )

        # Create recognizer
        self.recognizer = GestureRecognizer.create_from_options(options)
        print("Controller initialized ✅")

    # Callback when gesture is recognized
    def _result_callback(self, result: GestureRecognizerResult, output_image: mp.Image, timestamp_ms: int):
        if result.gestures:
            top_gesture = result.gestures[0][0].category_name

            # Only check for Open_Palm
            if top_gesture == "Open_Palm":
                self.last_gesture = top_gesture

                # Print only if new detection (avoid spam)
                if self.last_gesture != self.prev_gesture:
                    print(f"Detected: {top_gesture} (score={result.gestures[0][0].score:.2f})")
                    self.prev_gesture = self.last_gesture
            else:
                # Reset if other gesture appears
                self.last_gesture = None
                self.prev_gesture = None

    # Update camera + recognizer
    def update(self):
        ret, frame = self.cam.read()
        if not ret:
            print("Camera read error")
            return False

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        mp_img = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)

        # Send to recognizer
        self.recognizer.recognize_async(mp_img, int(time.time() * 1000))

        # Show webcam feed
        cv2.imshow("Cam", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            return False
        return True

    def get_gesture(self):
        """Return the last detected gesture (or None if nothing yet)."""
        return self.last_gesture

    def stop(self):
        self.cam.release()
        cv2.destroyAllWindows()
        print("Controller stopped ❌")
