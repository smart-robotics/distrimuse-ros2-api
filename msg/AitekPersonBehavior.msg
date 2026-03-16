# Information about a detected person's behavior, provided by Aitek
string STANDING_STILL = STANDING_STILL
string SITTING = SITTING
string LAYING_DOWN = LAYING_DOWN
string WALKING = WALKING
string RUNNING = RUNNING
string BENDING_OVER = BENDING_OVER
string FALLING = FALLING

string type             # Behavior type (e.g. STANDING, LAYING_DOWN, ...)
float32 confidence      # Confidence score of behavior type (0.0 to 1.0) (-1.0 if not used)
