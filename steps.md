accounts:
    - Model User
    - User
        -username
        -password
        -email
        -first_name
        -last_name

    Profile
        -user (One to One)
        -phone
        -address 
        Signals  
            -pre_save
            -post_save

    Views: ------> advanced
        - register
        - login_view
        - logout_view
        - forget_password
        - reset_password    

        1- register:
                - email
                - username
                - password
                - confirm password   



## Store
    -Category
        -name
        -slug

    - Size
        -name
    - Color
        -name        
    -Product
        - user
        - name
        - slug
        - category
        - price
        - size
        - color
        - stock
        - created_at
        - updated_at
        - is_available

    Image
        -product
        -image   

# Online Coaching
CRUD 
Create Retrieve Update Delete