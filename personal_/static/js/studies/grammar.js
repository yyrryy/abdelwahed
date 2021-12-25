const exercices=[
    {
        q:"_______________________ the latest news? <br>– The president ______________________ that he _____________________ to resign next summer. <br>– That's not new. I _____________________  that for ages!",
        ch:["YOU HEAR", "JUST ANNOUCE", "PLAN", "KNOW"],
        a:"Have you heard the latest news? – The president has just announced that he is planning to resign next summer. – That's not new. I have known that for ages!",
        h:['Have you heard', 'has just announced', 'is planning', 'have known'],
        e:['have you heard: ',
        'has just announced: ',
        'is planning: ',
        'have known: '
        ]
    },
    {
        q:'When she came home her two boys _____________________ football in the backyard. ',
        ch:["PLAY"],
        a:"Wen she came home her tow boys were playing football in the backyard",
        h:['were playing'],
        e:['were playin: ']
    },
    {
        q:"He _____________________ in hospital for a few days and the doctor said he _____________________ come home on Monday.",
        ch:["BE", "BE ABLE TO"],
        a:"He has been in hospital for a few days and the doctor said he whould be able to come home on Monday",
        h:['has been', 'whould be able to'],
        e:["him being in the hospital is an action that starts in the past and didn't finish yet (there is a 'for' indicator", 'zxpl for would']
    },
    {
        q:"The whole family _____________________ a few days ago and _____________________ with us until next Monday.",
        ch:["ARRIVE", "STAY"],
        a:"The whole family arrived a few days ago and are staying/will be staying/are going to stay/will stay with us until next Monday.",
        h:['arrived', 'are staying/will be staying/are going to stay/will stay'],
        e:["him being in the hospital is an action that starts in the past and didn't finish yet (there is a 'for' indicator", 'zxpl for would']
    },
    {
        q:"I _____________________ to call you all morning. Where _____________________?",
        ch:["TRY", "YOU BE"],
        a:"I have been trying to call you all morning. Where have you been?",
        h:['have been trying', 'have you been'],
        e:["him being in the hospital is an action that starts in the past and didn't finish yet (there is a 'for' indicator", 'zxpl for would']
    },
    {
        q:"We _____________________ enough money if everyone gives us €5",
        ch:["have"],
        a:"We will have enough money if everyone gives us €5",
        h:['will have'],
        e:["him being in the hospital is an action that starts in the past and didn't finish yet (there is a 'for' indicator", 'zxpl for would']
    },
    {
        q:"There _________________ a very good documentary on TV last night.<br> – _____________________ it? No, I _____________________ for my exam all night",
        ch:["be", "you see", "study"],
        a:"There was a very good documentary on TV last night.<br> – did you see it? No, I was studying for my exam all night",
        h:['was', 'did you see', 'was studying'],
        e:["", "", ""]
    },
    {
        q:"John Grisham is a famous author who _____________________ several thrillers. His latest book _____________________ out a few months ago.",
        ch:["write", "come"],
        a:"John Grisham is a famous author who has written several thrillers. His latest book came out a few months ago.",
        h:['has written', 'came'],
        e:[""]
    },
    {
        q:"",
        ch:[""],
        a:"",
        h:[''],
        e:[""]
    },
    {
        q:"",
        ch:[""],
        a:"",
        h:[''],
        e:[""]
    },
    {
        q:"",
        ch:[""],
        a:"",
        h:[''],
        e:[""]
    },
    {
        q:"",
        ch:[""],
        a:"",
        h:[''],
        e:[""]
    },
    {
        q:"",
        ch:[""],
        a:"",
        h:[''],
        e:[""]
    },
    
    
]

function highlight(ll, tar) {
  let holder= document.querySelector(tar)
  var innerHTML = holder.innerHTML;
  for (let text of ll){
      var index = innerHTML.indexOf(text);
        if (index >= 0) { 
        innerHTML = innerHTML.substring(0,index) + "<span class='answer'>" + innerHTML.substring(index,index+text.length) + "</span>" + innerHTML.substring(index + text.length);
        holder.innerHTML = innerHTML;
  }
  }
}
let exholder=$('.exholder')

exercices.map((ex, i)=>{
    expl=[]
    for (let j=0; j<ex.e.length; j++){expl.push(`<li>${ex.h[j]}: ${ex.e[j]}</li>`)}
    exholder.append(`
        <div>
            <p>${i+1}. ${ex.q}  <span class="text-primary">(${ex.ch.join(', ')})</span></p>
            
           <div class="tabs mb-5">
                <div class="tab ">
                    <input hidden type="checkbox" id="tt${i}">
                    <label class="tab-label" for="tt${i}">check</label>
                    <div class="tab-content">
                        <span class='answer${i}'>${ex.a}</span>
                        <div class="tabs">
                            <div class="tab">
                                <input hidden type="checkbox" id="expl${i}">
                                <label class="tab-label" for="expl${i}">Explination</label>
                                <div class="tab-content">
                                    ${expl.join('<br>')}
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
           </div>
        </div>
        
    `)
    highlight(ex.h, `.answer${i}`)
})