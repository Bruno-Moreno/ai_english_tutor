# Clone the repository 
git clone https://github.com/ggml-org/whisper.cpp.git 

# Navigate to the repository 
cd whisper.cpp 

# Download the model 
sh ./models/download-ggml-model.sh base.en
sh ./models/download-ggml-model.sh medium.en

# Build 
cmake -B build
cmake --build build -j --config Release

# Transcribe
./build/bin/whisper-cli -f ../audio/jfk.wav