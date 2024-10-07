from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/git',methods=['POST'])
def actualizar():
    data = request.json
    if data['ref'] == 'refs/heads/dev':
        try:
            subprocess.run(['git','-C','/data/hab-gac01','pull'], check=True)
            subprocess.run(['pm2','restart','vite'], check=True)
            return 'Proceso actualizado con éxito', 200
        except subprocess.CalledProcessError as e:
            return f'Error: {e}', 500
    return 'No es rama DEV', 200

@app.route('/',methods=['GET'])
def test():
    return 'Flask funcionando', 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
