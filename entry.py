from project import create_app

app = create_app(config='../local.cfg')

if __name__ == '__main__':
    app.run()
