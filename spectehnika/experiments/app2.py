from dataclasses import dataclass

from flask import Flask, render_template, request

app2 = Flask(__name__)


@dataclass
class Machine:
    id: int
    name: str
    user: str
    number: str


machines = [
    Machine(1, 'Tech1', 'Driver1', 'abc123'),
    Machine(2, 'Tech2', 'Driver2', 'abc456'),
    Machine(3, 'Tech3', 'Driver3', 'abc789'),
]


@app2.get('/')
def index():
    return render_template('index.html', machines=machines)


@app2.get('/machine')
def get_machine():
    machine_id = int(request.args.get('id'))
    machine = [machine for machine in machines if machine.id == machine_id][0]
    return render_template('get_machine.html', machine=machine)


@app2.get('/edit_machine')
def edit_machine():
    machine_id = int(request.args.get('id'))
    machine = [machine for machine in machines if machine.id == machine_id][0]
    return render_template('edit_machine.html', machine=machine)


@app2.patch('/machine')
def patch_machine():
    ...


@app2.delete('/machine')
def delete_machine():
    return ''


app2.run(debug=True)
