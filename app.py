from flask import Flask, render_template
from day1.routes import day1_bp
from day2.routes import day2_bp
from day3.routes import day3_bp
from day4.routes import day4_bp
from day5.routes import day5_bp
from day6.routes import day6_bp
from day7.routes import day7_bp
from day8.routes import day8_bp
from day9.routes import day9_bp
from day10.routes import day10_bp
from day11.routes import day11_bp
from day12.routes import day12_bp
from day13.routes import day13_bp
from day14.routes import day14_bp

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(day1_bp, url_prefix='/day1')
app.register_blueprint(day2_bp, url_prefix='/day2')
app.register_blueprint(day3_bp, url_prefix='/day3')
app.register_blueprint(day4_bp, url_prefix='/day4')
app.register_blueprint(day5_bp, url_prefix='/day5')
app.register_blueprint(day6_bp, url_prefix='/day6')
app.register_blueprint(day7_bp, url_prefix='/day7')
app.register_blueprint(day8_bp, url_prefix='/day8')
app.register_blueprint(day9_bp, url_prefix='/day9')
app.register_blueprint(day10_bp, url_prefix='/day10')
app.register_blueprint(day11_bp, url_prefix='/day11')
app.register_blueprint(day12_bp, url_prefix='/day12')
app.register_blueprint(day13_bp, url_prefix='/day13')
app.register_blueprint(day14_bp, url_prefix='/day14')

# Home Page Route
@app.route("/")
def index():
    return render_template("index.html", total_days=13)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
