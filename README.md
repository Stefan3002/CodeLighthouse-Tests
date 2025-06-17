# CodeLighthouse Selenium Test Suite

This repository contains automated end-to-end (E2E) test cases written using **Selenium WebDriver** for the **CodeLighthouse** platform. These tests were developed as part of the practical validation process for my **Bachelor's thesis**, which focused on developing a real-time code feedback and educational platform.

---

## 📚 Project Context

The tests target the **CodeLighthouse** web application, which provides functionality for:

- Real-time code evaluation
- Assignment submissions
- Feedback delivery
- Role-based dashboards for students and instructors

These tests ensure that core user flows behave as expected and help validate the reliability of the platform under real-world usage scenarios.

---

## ⚙️ Technologies Used

- **Selenium WebDriver**
- **Python 3.x**

---

## 🧪 Test Scenarios

Here are some of the key functional areas covered by the test suite:

- Login with valid and invalid credentials
- Logout functionality
- Redirect behavior on unauthorized access
- Button functions

---

## 🚀 Running the Tests

Make sure you have ChromeDriver installed and accessible in your system `PATH`.

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run tests with:
   ```bash
   python -m unittest discover
   ```

Or with pytest:
```bash
pytest
```

---

## 📎 Note

These tests assume that the CodeLighthouse app is running locally on the expected port. You may need to update base URLs in the test setup accordingly.

---

## 📄 License

This repository is part of the deliverables for my undergraduate thesis and is shared for academic and reference purposes.

---

## 🙋‍♂️ Author

**Ștefan Secrieru**  
GitHub: [@Stefan3002](https://github.com/Stefan3002)  
Thesis: CodeLighthouse - Automated Online Assessments Platform
