from flask import Flask, render_template, redirect, url_for, request, flash, session
from forms import RegistrationForm, LoginForm, PaymentForm, FeedbackForm, AnimalForm
from functools import wraps
import pymysql
import os




app = Flask(__name__)

app.config['SECRET_KEY'] = os.urandom(16)


db = pymysql.connect("localhost", "root", "", "website2")

#login authentication
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login first.', 'danger')
            return redirect(url_for('login'))
    return wrap

#home page
@app.route('/')
def index():
    return render_template('index.html')


#about us
@app.route('/about')
def about():
    return render_template('about.html')


#contact page
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = FeedbackForm()
    if request.method == 'POST' and form.validate_on_submit():
        rating = request.form['rating']
        feed_type = request.form['feed_type']
        comment = request.form['comment']
        feed_email = request.form['feed_email']

        cursor = db.cursor()
        try:
            cursor.execute("INSERT INTO feedback (rating,feed_type,comment,feed_email) VALUES (%s,%s,%s,%s)", (rating,feed_type,comment,feed_email))
            #save changes
            db.commit()
            cursor.close()
            flash(f'Feedback submitted.', 'success')
        except:
            flash(f'Email is invalid. Please try again.', 'danger')
        return redirect(url_for('contact'))
    return render_template('contact.html', form=form)





#list of accounts
@app.route('/users', methods=['GET', 'POST'])
@is_logged_in
def users():
    cursor = db.cursor()
    try:
        sql = ("SELECT * FROM website")
        cursor.execute(sql)
        results = cursor.fetchall()
        return render_template('users.html', results = results)
    except:
        return redirect(url_for('register'))

#list of animals
@app.route('/animalslist', methods=['GET', 'POST'])
@is_logged_in
def animalslist():
    cursor = db.cursor()

    cursor.execute("SELECT * FROM animal")
    results = cursor.fetchall()
    return render_template('animalslist.html', results = results)

#fund statistics of animals
@app.route('/animals', methods=['GET', 'POST'])
@is_logged_in
def animals():
    cursor = db.cursor()

    cursor.execute("SELECT animal_name from payment\
    GROUP BY animal_name;")
    names = cursor.fetchall()
    #left join from payment to animal
    sql = ("SELECT animal.animal_id, payment.animal_name, animal.years_old, animal.disease, SUM(payment.money) AS 'Total Money'\
    FROM payment\
    LEFT JOIN animal \
    ON payment.animal_name = animal.animal_name\
    GROUP BY animal_name\
    ORDER BY animal_id;")
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template('animals.html', names = names, results = results)

#add animal
@app.route('/addanimal', methods=['GET', 'POST'])
@is_logged_in
def addanimal():
    form = AnimalForm()
    if request.method == 'POST' and form.validate_on_submit():
        animal_name = request.form['animal_name']
        years_old = request.form['years_old']
        disease = request.form['disease']
        cursor = db.cursor()
        cursor.execute("INSERT INTO animal (animal_name,years_old,disease) VALUES (%s,%s,%s)", (animal_name,years_old,disease))
        db.commit()
        cursor.close()
        flash('Animal created', 'success')
        return redirect(url_for('animalslist'))
    return render_template('addanimal.html', form=form)

#edit animal info
@app.route('/edit_animal/<string:animal_id>', methods=['GET', 'POST'])
@is_logged_in
def edit_animal(animal_id):

    cursor = db.cursor()

    #get animal by id
    result = cursor.execute("SELECT * FROM animal WHERE animal_id = %s", [animal_id])

    user = cursor.fetchone()
    cursor.close()
    #get form
    form = AnimalForm(request.form)

    #populate animal data
    form.animal_name.data = user[1]
    form.years_old.data = user[2]
    form.disease.data = user[3]


    if request.method == 'POST' and form.validate_on_submit():
        animal_name = request.form['animal_name']
        years_old = request.form['years_old']
        disease = request.form['disease']


        cursor = db.cursor()
        #update data of the selected id in database
        cursor.execute("UPDATE animal SET animal_name=%s, years_old=%s, disease=%s WHERE animal_id=%s",(animal_name, years_old, disease, animal_id))

        db.commit()
        cursor.close()

        flash('Animal Updated', 'success')

        return redirect(url_for('animalslist'))

    return render_template('edit_animal.html', form = form)

#delete animal from list
@app.route('/delete_animal/<string:animal_id>', methods=['POST'])
@is_logged_in
def delete_animal(animal_id):

    cursor = db.cursor()


    cursor.execute("DELETE FROM animal WHERE animal_id = %s", [animal_id])


    db.commit()
    cursor.close()


    flash('Animal Deleted', 'success')

    return redirect(url_for('animalslist'))

#payment history
@app.route('/paycheck', methods=['GET', 'POST'])
@is_logged_in
def paycheck():
    cursor = db.cursor()
    sql = ("SELECT * FROM payment")
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template('paycheck.html', results = results)

#register page
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()



    if request.method == 'POST' and form.validate_on_submit():
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        cursor = db.cursor()
        try:
            cursor.execute("INSERT INTO website (username,email,password) VALUES (%s,%s,%s)", (username,email,password))
            db.commit()
            cursor.close()
            flash(f'Account created for {form.username.data}!', 'success')
        except:
            flash(f'Account is duplicated. Please change username or email.', 'danger')
        return redirect(url_for('register'))
    return render_template('register.html', form=form)


#payment form
@app.route("/paymenttest", methods=['GET', 'POST'])
@is_logged_in
def paymenttest():
    form = PaymentForm()
    if request.method == 'POST' and form.validate_on_submit():

        name = request.form['name']

        credit_type = request.form['credit_type']
        credit_no = request.form['credit_no']
        expir_month = request.form['expir_month']
        expir_year = request.form['expir_year']
        cvv = request.form['cvv']
        money = request.form['money']
        animal_name = request.form['animal_name']


        cursor = db.cursor()
        try:
            #insert the payment data to the database
            cursor.execute("INSERT INTO payment (name,username,credit_type,credit_no,expir_month,expir_year,cvv,money,animal_name) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)", (name,session["username"],credit_type,credit_no,expir_month,expir_year,cvv,money,animal_name))
            db.commit()
            cursor.close()
            flash(f'Payment succeed!', 'success')
        except:
            flash(f'Payment failed. Please try again.', 'danger')
        return redirect(url_for('paymenttest'))
    return render_template('paymenttest.html', form=form)

#must login before entering the payment page
@app.route('/paymentverify')
def paymentverify():
    if "username" in session:
        username = session["username"]
        flash(f'Welcome {username}!', 'success')
        return redirect(url_for('paymenttest'))
    else:
        flash('Please login first.', 'danger')
        return redirect(url_for('login'))



#login page
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():

        if request.method == 'POST':
            username = request.form['username']
            password_candidate = request.form['password']


            cursor = db.cursor()
            #verify whether the username is match with the password
            result = cursor.execute('SELECT * FROM website WHERE username = %s', (username))
            if result > 0:
                data = cursor.fetchone()
                password = data[3]

                if password_candidate == data[3]:
                    session["logged_in"] = True
                    session["username"] = username
                    flash('You have been logged in!', 'success')
                    return redirect(url_for('login'))
                else:
                    flash('Login Unsuccessful. Please check the password.', 'danger')
                    return redirect(url_for('login'))
            else:
                flash('Login Unsuccessful. Username does not exist.', 'danger')
                return redirect(url_for('login'))
                cursor.close()




    return render_template('login.html', form=form)


#edit users' accounts
@app.route('/edit_account/<string:id>', methods=['GET', 'POST'])
@is_logged_in
def edit_account(id):

    cursor = db.cursor()

    #get user by id
    result = cursor.execute("SELECT * FROM website WHERE id = %s", [id])

    user = cursor.fetchone()
    cursor.close()
    #get registration form
    form = RegistrationForm(request.form)

    #populate user's data
    form.username.data = user[1]
    form.email.data = user[2]


    if request.method == 'POST' and form.validate_on_submit():
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']


        cursor = db.cursor()
        # Execute
        cursor.execute("UPDATE website SET username=%s, email=%s, password=%s WHERE id=%s",(username, email, password, id))
        # Commit to DB
        db.commit()
        cursor.close()

        flash('Account Updated', 'success')


        return redirect(url_for('users'))
    return render_template('edit_account.html', form = form)

#delete account
@app.route('/delete_account/<string:id>', methods=['POST'])
@is_logged_in
def delete_account(id):

    cursor = db.cursor()

    #delete from database
    cursor.execute("DELETE FROM website WHERE id = %s", [id])

    db.commit()
    cursor.close()


    flash('Account Deleted', 'success')

    return redirect(url_for('users'))

#logout
@app.route('/logout')
@is_logged_in
def logout():
    if "username" in session:
        session.pop("username", None)
        flash('Logged out successfully.', 'success')
        return redirect(url_for('login'))
    else:
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
