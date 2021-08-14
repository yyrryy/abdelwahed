from flask import Flask, request, render_template, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os
from urllib.parse import urlparse


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('abdelouaheddb')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY']=os.environ.get('SECRET_KEY')



db = SQLAlchemy(app)
bcrypt  = Bcrypt(app)

from personal_.admin.routes import admin
from personal_.main.routes import main
from personal_.blog.routes import log

app.register_blueprint(admin)
app.register_blueprint(main)
app.register_blueprint(log)

from personal_.models import Posts

@app.route("/sitemap")
@app.route("/sitemap/")
@app.route("/sitemap.xml")
def sitemap():
    """
        Route to dynamically generate a sitemap of your website/application.
        lastmod and priority tags omitted on static pages.
        lastmod included on dynamic content such as blog posts.
    """
    

    host_components = urlparse(request.host_url)
    host_base = host_components.scheme + "://" + host_components.netloc
    
    # Static routes with static content
    static_urls = list()
    for rule in app.url_map.iter_rules():
    
        if not str(rule).startswith("/admin") and not str(rule).startswith("/blog/") and not str(rule).startswith("/sitemap") and not str(rule).startswith("/static"):
            if "GET" in rule.methods and len(rule.arguments) == 0:
                url = {
                    "loc": f"{host_base}{str(rule)}"
                }
                static_urls.append(url)
    
    # Dynamic routes with dynamic content
    dynamic_urls = []
    products = Posts.query.all()
    shop= {
        "loc": f"{host_base}/blog/",
    }
    dynamic_urls.append(shop)
    for product in products:
        
        url = {
            "loc": f"{host_base}/blog/post/{product.id}/{product.title}",
            }
        dynamic_urls.append(url)
    xml_sitemap = render_template("sitemap.xml", static_urls=static_urls, dynamic_urls=dynamic_urls, host_base=host_base)
    response = make_response(xml_sitemap)
    response.headers["Content-Type"] = "application/xml"

    return response
 