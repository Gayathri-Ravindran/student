from django.db import models
from django.contrib.auth.models import User  # Import the built-in User model for user authentication

# Define the Department model
class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Define the Course model
class Course(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Define the UserProfile model for custom user information
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    # Add any additional user-related fields here, if needed
    # For example: phone_number, address, etc.

    def __str__(self):
        return self.user.username



class Order(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    phone = models.CharField(max_length=10)
    mail_id = models.EmailField()
    address = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    purpose = models.CharField(max_length=100, choices=[('Enquiry', 'Enquiry'), ('Place Order', 'Place Order'), ('Return', 'Return')])

    def __str__(self):
        return self.name
