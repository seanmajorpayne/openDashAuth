from app import create_app

app = create_app()
from app.plotlydash.dashboard import create_dashboard

app = create_dashboard(app)
