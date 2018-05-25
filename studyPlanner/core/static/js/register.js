function registerUser(){
    var email = $("#txtEmail").val()
    var password = $("#txtPassword").val()
    var username = $("#txtUser").val()

    //fazer validação da senha
    createFirebaseUser(email,password, username)
}

function redirectUser(){

    
}