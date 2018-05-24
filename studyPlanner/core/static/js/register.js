function registerUser(){
    var email = $("#txtEmail").val()
    var password = $("#txtPassword").val()

    //fazer validação da senha
    console.log(email)
    console.log(password)
    createFirebaseUser(email,password)
}

function redirectUser(){

    
}