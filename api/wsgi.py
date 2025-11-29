from vercel_wsgi import Handler as VercelHandler
from main import app

handler = VercelHandler(app)
