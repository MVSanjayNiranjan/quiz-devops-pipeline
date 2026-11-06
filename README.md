# Quiz Management System – DevOps pipeline (Practicum 10)

Every push runs a GitHub Actions pipeline: **lint → unit tests with coverage + Bandit security scan → Docker build → Trivy image scan**.

```bash
pip install -r requirements-dev.txt
pytest --cov=quiz_system
```
