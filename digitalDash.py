from app import create_app

app = create_app()
from app.plotlydash.dashboard import create_dashboard  # Do not move to top of file
app = create_dashboard(app)
