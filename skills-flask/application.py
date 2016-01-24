from flask import Flask, render_template, request

app = Flask(__name__)
# 30 minutes

@app.route("/")
def index_page():
    """Show an index page."""

    return "<html><body>This is the homepage.</body></html>"

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")

@app.route("/application-form")
def form_page():
    """
    Renders application-form.html with form a <form> that can capture
    the first name, last name, job title, and salary requirement data.
    """

    return render_template("application-form.html")


@app.route("/application-response", methods=["POST"])
def application_page():
    """ Handles submission of a form in application-form.html to /application.

    Gets the first name, last name, salary, and job title from the request.
    Returns a response that acknowledges their application.

    This should repeat their name, title, and salary requirement, like:

    Thank you, Jessica McHackbright, for applying to be a QA Engineer. Your
    minimum salary requirement is 89000 dollars.

    """

    firstname = request.form.get("FirstName")
    lastname = request.form.get("LastName")
    salary = request.form.get("Salary")
    job = request.form.get("job")
    print firstname, lastname, salary, job

    return render_template("application-response.html",
                            firstname=firstname,
                            lastname=lastname,
                            salary=salary,
                            job=job,
                            )

if __name__ == "__main__":
    app.run(debug=True)
