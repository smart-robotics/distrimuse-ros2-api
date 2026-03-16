# Information about the activity of a person, provided by Pumacy
string STANDING_STILL = STANDING_STILL
string SITTING = SITTING
string LAYING_DOWN = LAYING_DOWN
string WALKING = WALKING
string RUNNING = RUNNING
string BENDING_OVER = BENDING_OVER
string FALLING = FALLING

string type             # Activity type (e.g. STANDING, RUNNING, ...)
float32 confidence      # Confidence score of activity type (0.0 to 1.0) (-1.0 if not used)
bool anomalous          # Whether the activity is considered an anomaly (true) or normal behavior (false) 
