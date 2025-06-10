### virtual environment using uv 
```python
!pip install uv
uv init sqlproj
cd sqlproj
uv -r requirements.txt
!uv run main.py
```
### Create a new gitub repository and push the code
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin <your-github-repo-url>
git push -u origin main / master (for older repository)
```