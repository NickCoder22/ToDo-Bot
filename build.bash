cd database
marutin build -o ../wheels
cd ..
pip install wheels/$(ls -1 wheels | head -n 1)
pip install -r requirements.txt