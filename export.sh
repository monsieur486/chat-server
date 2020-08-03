find . -type d -name "__pycache__" -exec rm -Rf {} \;
find . -type d -name "*.pyc" -exec rm -Rf {} \;
git add .
git commit -m "last compilation"
