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