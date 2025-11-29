from vercel_wsgi import VercelHandler
from main import app

handler = VercelHandler(app)