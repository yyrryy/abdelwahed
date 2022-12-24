from personal_ import app
import os


if __name__ == '__main__':
    app.debug= os.environ.get('DEBUG')
    app.run('0.0.0.0', port=5000)

