const question_show_box=document.getElementById("question-show-box")
const image_A=document.getElementById("imageA")
const image_B=document.getElementById("imageB")
const otherCount=document.getElementById("other-count")
const load_more_questions=document.getElementById("load-more-questions")
const spinner_box_questions=document.getElementById("spinner-box-questions")

const vote = () => {
 
   buttons=[
    ...document.getElementsByClassName("buttons-f"),
  ];
 
  
 
  buttons.forEach((button) =>
    button.addEventListener("click", (e) => {
      e.stopImmediatePropagation();
      e.preventDefault();
      const btnId = e.target.getAttribute("data-btn-id");
      const btnType = e.target.getAttribute("data-btn-type");
      clickedBtn= e.target
     let otherBtnType=""
       
      if(btnType=="A"){
        otherBtnType="B"
      }
      else if(btnType=="B"){
        otherBtnType="A"
      }
    
      // setTimeout(function(){
      
    // },5000)

      
     
       
      console.log("otherBtn",otherBtnType)
     
      console.log("btnId",btnId)
      console.log("btntype",btnType)


      $.ajax({
        type: "POST",
        url: "vote/",
        data: {
          csrfmiddlewaretoken: csrftoken,
          btnId: btnId,
          btnType:btnType
        },
        success: function (response) {
          console.log(response);
          
          if(btnType=="A"){
          clickedBtn.innerHTML = `
                ${
                  response.voteA
                    ? `Voted (${
                        response.countA < 999
                          ? response.countA
                          : numeral(response.countA).format("0.0a")
                      })`
                    : `Vote (${
                        response.countA < 999
                          ? response.countA
                          : numeral(response.countA).format("0.0a")
                      })`
                }`;
            otherCount.value=response.otherCount
            buttons.forEach((button)=>{
              if(button.getAttribute("data-btn-id")==btnId && button.getAttribute("data-btn-type")==otherBtnType){
                 button.innerHTML=`${response.is_votedB ?`Voted (${otherCount.value<999?otherCount.value:numeral(otherCount.value).format("0.0a")})`:
                 `Vote (${otherCount.value<999?otherCount.value:numeral(otherCount.value).format("0.0a")})`}`
                console.log("trueAf",otherCount.value)
              }
              
            })

            console.log("other-count",otherCount.value)
              }

              if(btnType=="B"){
                clickedBtn.innerHTML = `
                      ${
                        response.voteB
                          ? `Voted (${
                              response.countB < 999
                                ? response.countB
                                : numeral(response.countB).format("0.0a")
                            })`
                          : `Vote (${
                              response.countB < 999
                                ? response.countB
                                : numeral(response.countB).format("0.0a")
                            })`
                      }`;
                      otherCount.value=response.otherCount

                      buttons.forEach((button)=>{
                        if(button.getAttribute("data-btn-id")==btnId && button.getAttribute("data-btn-type")==otherBtnType){
                           button.innerHTML=`${response.is_votedA ?`Voted (${otherCount.value<999?otherCount.value:numeral(otherCount.value).format("0.0a")})`:
                           `Vote (${otherCount.value<999?otherCount.value:numeral(otherCount.value).format("0.0a")})`}`
                          console.log("trueAf",otherCount.value)
                        }
                        
                      })
                      console.log("other-count",otherCount.value)
                    }
          
        },
        error: function (error) {
          console.log(error);
        },
      });
    })
  );
};



let dyna_visible_questions=5

const getQuestions=()=>{

    $.ajax({
        url:`get-questions/${dyna_visible_questions}/`,  
        success:function(response) {
           console.log("questions",response)
           setTimeout(() => {
           spinner_box_questions.classList.add("not-visible");
           data=response.data
           data.forEach(function(question){
           question_show_box.innerHTML+=`
            
           

           <div class="container mb-2">
             

           <div class="row border-1 border-bottom p-2 border-success mb-2 ">  
           <div>
           <h4 class="text-center mb-3"> ${question.question}</h4>   
          </div>
            <div class="col-6 p-1">
           <div class="float-end" id="imageADiv">
           <img  id="imageA" src="${question.imageA}">
 
           <button data-btn-id=${question.id} data-btn-type="A" class='voteA btn btn-primary  buttons-f  mt-1 float-start  border none  rounded' id="voteA">
           ${
            question.is_votedA
              ? `Voted (${
                  question.countA < 999
                    ? question.countA
                    : numeral(question.countA).format("0.0a")
                })`
              : `Vote (${
                  question.countA < 999
                    ? question.countA
                    : numeral(question.countA).format("0.0a")
                })`
          }
           
           </button>
           <br>
          </div>
          
 
            </div>
           
           <div class="col-6 p-1"> 
          <div id="imageBDiv" class="text-start">
           
           <img class="img-fluid" id="imageB" src="${question.imageB}"  >
           <button data-btn-id=${question.id} data-btn-type="B" class=' voteB buttons-f  btn btn-primary mt-1 float-start  border none  rounded' id="voteB"> 
           ${
            question.is_votedB
              ? `Voted (${
                  question.countB < 999
                    ? question.countB
                    : numeral(question.countB).format("0.0a")
                })`
              : `Vote (${
                  question.countB < 999
                    ? question.countB
                    : numeral(question.countB).format("0.0a")
                })`
          }
             
             </button>
           <br>
 </div>
 </div>       
       </div>  
       
  </div><br><br><br><br>`      
        
        });

        vote();
      }, 1000);

      if (response.size === 0) {
        load_more_questions.classList.add("not-visible");
      } else if (response.size <= dyna_visible_questions) {
        load_more_questions.classList.add("not-visible");
      }
        
      
    
        },
        error:function(error) {
           
      }
  
  });
   


}

$("#load-more-questions")
.unbind("click")
.bind("click", function (e) {
  e.stopImmediatePropagation();
  spinner_box_questions.classList.remove("not-visible");

  dyna_visible_questions += 5;
   
  getQuestions()
});

getQuestions()