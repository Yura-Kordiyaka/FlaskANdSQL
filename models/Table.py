from app import db


class Employees(db.Model):
    _tablname_ = 'zemployees'
    employee_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(70), nullable=True)
    last_name = db.Column(db.String(70), nullable=True)
    Email = db.Column(db.String(70), nullable=True)
    phone_number = db.Column(db.String(70), nullable=True)
    hire_date = db.Column(db.DateTime, nullable=True)
    job_id = db.Column(db.Integer, nullable=True)
    salary = db.Column(db.Integer, nullable=True)
    commission_pct = db.Column(db.Integer, nullable=True)
    manager_id = db.Column(db.Integer, nullable=True)
    department_id = db.Column(db.Integer, nullable=True)

    @property
    def serialize(self):
        return {
            'employee id': self.employee_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'Email': self.Email,
            'phone_number': self.phone_number,
            'hire_date': self.hire_date,
            'job_id': self.job_id,
            'salary': self.job_id,
            'commission_pct': self.commission_pct,
            'manager_id': self.manager_id,
            'department_id': self.department_id
        }

    @property
    def fname(self):
        return self.first_name

    @property
    def lname(self):
        return self.last_name

    @property
    def hire(self):
        return self.hire_date

    @property
    def get_email(self):
        return self.Email
