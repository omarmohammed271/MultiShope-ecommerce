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

    Views: ------> advanced
        - register
        - login_view
        - logout_view
        - forget_password
        - reset_password       

Signals  
    -pre_save
    -post_save