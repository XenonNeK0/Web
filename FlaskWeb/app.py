# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

# 配置项（可选）
app.config["DEBUG"] = True  # 开启调试模式，这样代码变动后服务器会自动重启


# 路由和视图函数
@app.route("/")
def home():
    return render_template("index.html")  # 渲染模板文件


@app.route("/greet", methods=["GET", "POST"])
def greet():
    if request.method == "POST":
        name = request.form["name"]  # 从表单中获取数据
        return f"Hello, {name}!"
    return render_template("greet.html")  # 渲染表单模板


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # 在所有网络接口上运行，监听5000端口
