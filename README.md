# Dockerized Python Hello World Web Server

This project is a portfolio example demonstrating secure Docker containerization of a simple Python web server. It highlights foundational DevSecOps practices such as:

- Using a non-root user inside the container
- Building a minimal, self-contained image
- Serving a simple Python HTTP application

> 🛡️ This project is intended solely for demonstration purposes to showcase skills in Docker and Python. It is not production hardened.

---

## 🔧 How It Works

The container runs a lightweight `http.server`-based application in Python that responds with:

```

Hello, World from Docker!

````

---

## 🚀 Getting Started

### Build the Image

```bash
docker build -t hello-server .
````

### Run the Container

```bash
docker run -p 8080:8080 hello-server
```

Then open your browser to [http://localhost:8080](http://localhost:8080)

---

## 🧱 Project Structure

```
.
├── app.py              # Python web server
├── Dockerfile          # Container build script
└── README.md           # You're reading it
```

---

## 🔐 Security Best Practices Included

* Runs as a non-root user
* Uses a minimal base image (`ubuntu:22.04`)

---

## 📜 License

This project is released under the [MIT License](LICENSE).