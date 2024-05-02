from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

# Load benchmark data from JSON file
def load_benchmarks():
    with open('data/benchmarks.json') as f:
        benchmarks = json.load(f)
    return benchmarks

# Save benchmark data to JSON file
def save_benchmarks(benchmarks):
    with open('data/benchmarks.json', 'w') as f:
        json.dump(benchmarks, f, indent=4)

@app.route('/')
def index():
    benchmarks = load_benchmarks()
    return render_template('index.html', benchmarks=benchmarks)

@app.route('/add', methods=['GET'])
def show_add_benchmark():
    return render_template('add_benchmark.html')


@app.route('/add_benchmark_submit', methods=['POST'])
def add_benchmark():
    make = request.form['make']
    model = request.form['model']
    mining_software = request.form['mining_software']
    os = request.form['os']
    hashrate = request.form['hashrate']
    notes = request.form['notes']
    
    benchmark = {
        'make': make,
        'model': model,
        'mining_software': mining_software,
        'os': os,
        'hashrate': hashrate,
        'notes': notes
    }
    
    benchmarks = load_benchmarks()
    benchmarks.append(benchmark)
    save_benchmarks(benchmarks)
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
