# this is how you crate a constructor


class employee:
  def __init__(self):
    print("I am self employed")
  def __del__(self):
    print("deleted")
obj=employee()
del obj


    
  
