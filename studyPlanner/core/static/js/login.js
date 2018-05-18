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

// $(function(){
// var textfield = $("input[name=user]");
//             $('button[type="submit"]').click(function(e) {
//                 e.preventDefault();
//                 //little validation just to check username
//                 if (textfield.val() != "") {
//                     //$("body").scrollTo("#output");
//                     $("#output").addClass("alert alert-success animated fadeInUp").html("Welcome back " + "<span style='text-transform:uppercase'>" + textfield.val() + "</span>");
//                     $("#output").removeClass(' alert-danger');
//                     $("input").css({
//                     "height":"0",
//                     "padding":"0",
//                     "margin":"0",
//                     "opacity":"0"
//                     });
//                     //change button text 
//                     $('button[type="submit"]').html("continue")
//                     .removeClass("btn-info")
//                     .addClass("btn-default").click(function(){
//                     $("input").css({
//                     "height":"auto",
//                     "padding":"10px",
//                     "opacity":"1"
//                     }).val("");
//                     });
                    
//                     //show avatar
//                     /*$(".avatar").css({
//                         "background-image": "url('http://api.randomuser.me/0.3.2/portraits/women/35.jpg')"
//                     });*/
//                 } else {
//                     //remove success mesage replaced with error message
//                     $("#output").removeClass(' alert alert-success');
//                     $("#output").addClass("alert alert-danger animated fadeInUp").html("sorry enter a username ");
//                 }
//                 //console.log(textfield.val());

//             });
// });

