// Initialize Firebase
var config = {
    apiKey: "AIzaSyBBE__151mZb7-Dwm_YXlAgfVDhU2vcoUM",
    authDomain: "study-planner-app.firebaseapp.com",
    databaseURL: "https://study-planner-app.firebaseio.com",
    projectId: "study-planner-app",
    storageBucket: "study-planner-app.appspot.com",
    messagingSenderId: "455361032393"
  };

  firebase.initializeApp(config);

  function createFirebaseUser(email,password,username){
    firebase.auth().createUserWithEmailAndPassword(email, password)
    .then(function(){
      
      $.ajax({
        url: '/createUser/',
        data: {
          'email':email,
          'password':password,
          'username':username
        },
        dataType: 'json',
        success: function (data) {
        }
      });

    }).catch(function(error) {
      var errorCode = error.code;
      var errorMessage = error.message;
      alert(errorMessage)
    });
  }

 function loginWithGoogle(e){
    e.preventDefault();
    var provider = new firebase.auth.GoogleAuthProvider();

    firebase.auth().signInWithPopup(provider).then(function(result) {
        var token = result.credential.accessToken;
        var user = result.user;
       window.location.href = 'http://127.0.1:8000/alunos';
        
    }).catch(function(error) {
        var errorCode = error.code;
        var errorMessage = error.message;
        var email = error.email;
        var credential = error.credential;
        console.log(errorMessage)

      });

  }

  function loginWithFacebook(e){
    e.preventDefault();
    var provider = new firebase.auth.FacebookAuthProvider();
    firebase.auth().signInWithPopup(provider).then(function(result) {
        var token = result.credential.accessToken;
        var user = result.user;

       window.location.href = 'http://127.0.1:8000/alunos';

      }).catch(function(error) {
        var errorCode = error.code;
        var errorMessage = error.message;
        var email = error.email;
        var credential = error.credential;
      });
  }