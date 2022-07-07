let exholder=$('.exholder')
let presentholder=$('.presentholder')
let pastholder=$('.pastholder')
let futureholder=$('.futureholder')

const present=[
    {
        
        s:'Simple',

        u:[
            ['For habits', 'I drink tea at breakfast.'],
            ['For repeated actions or events', "I catch the bus every morning"],
            ['For general truths', "Water freezes at zero degrees."],
            ["For instructions or directions", "You walk for two hundred meters, then you turn left."],
            ["For fixed arrangements", "His mother arrives tomorrow."]
        ]
    },

    {   
        s:'Perfect',
        u:[
            ['Actions which started in the past and are still continuing', 'He has lived in Canada for five years'],
            ['Actions (single action or repeated actions) which happened at some unknown time in the past', "I've already seen that film. I don't want to see it again"],
            ['Actions which happened in the past, but have an effect in the present', "I've lost my keys."]
        ]
    },
    
    {
        
        s:'Progressive',
        u:[
           ['a current action, an action in progress or an unfinished action', 'The children are sleeping right now.'],
            ['It is often used for descriptions', "The jaguar is lying on a tree branch."]
        ]
    },
    
]  

const past=[
    {
        
        s:'Simple',

        u:[
            ["Finished actions in the past.", "I went to the cinema yesterday."]
        ]
    },

    {   
        s:'Perfect',
        u:[
            [
                "refer to something that happened more in the past than something else. We usually use the past perfect to make it clear which action happened first. Maybe we are already talking about something in the past and we want to mention something else that is further back in time. This is often used to explain or give a reason for something in the past.",
                "My brother sold his car on Saturday. He’d had it for 20 years!"
            ],
            [
                "Something that started in the past and continued up to another action or time in the past. The past perfect tells us 'how long', just like the present perfect, but this time the action continues up to a point in the past rather than the present. Usually we use 'for + time'. We can also use the past perfect continuous here, so we most often use the past perfect simple with <a href='#st'>stative verbs.</a>",
                "When he graduated, he had been in London for six years. (= He arrived in London six years before he graduated and lived there until he graduated, or even longer.)"
            ],
            [
                "To talk about unreal or imaginary things in the past. In the same way that we use the past simple to talk about unreal or imaginary things in the present, we use the past perfect (one step back in time) to talk about unreal things in the past. This is common in the third conditional and after 'wish'.",
                "If I had known you were ill, I would have visited you."
            ]
        ]
    },
    
    {
        
        s:'Progressive',
        u:[
            [
                "Continuous action in the past.",
                "I was walking to the station when I met John. (I started walking before I met John, and maybe I continued afterwards.)"
            ],
            [

            ]
        ]
    },
    
]  

const future=[
    {
        
        s:'Simple',

        u:[
            ['For habits', 'I drink tea at breakfast.'],
            ['For repeated actions or events', "I catch the bus every morning"],
            ['For general truths', "Water freezes at zero degrees."],
            ["For instructions or directions", "You walk for two hundred meters, then you turn left."],
            ["For fixed arrangements", "His mother arrives tomorrow."]
        ]
    },

    {   
        s:'Perfect',
        u:[
            ['Actions which started in the past and are still continuing', 'He has lived in Canada for five years'],
            ['Actions (single action or repeated actions) which happened at some unknown time in the past', "I've already seen that film. I don't want to see it again"],
            ['Actions which happened in the past, but have an effect in the present', "I've lost my keys."]
        ]
    },
    
    {
        
        s:'Progressive',
        u:[
            ['Actions which started in the past and are still continuing', 'He has lived in Canada for five years'],
            ['Actions (single action or repeated actions) which happened at some unknown time in the past', "I've already seen that film. I don't want to see it again"],
            ['Actions which happened in the past, but have an effect in the present', "I've lost my keys."]
        ]
    },
    
]  




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

present.map((v, i)=>{
    usage=[]
    ll=[]
    for (let i of v.u) {
        ll.push(i.join(': <br>'))
    }
    for (let i of ll){usage.push(`<li>${i}</li>`)}
    presentholder.append(`
    <div class="tab">
        <input hidden type="checkbox" id="${v.s}">
        <label class="tab-label" for="${v.s}">${v.s}</label>
        <div class="tab-content">
            ${usage.join('<br>')}
        </div>
    </div>
    `)
    
})

past.map((v, i)=>{
    usage=[]
    ll=[]
    for (let i of v.u) {
        ll.push(i.join(': <br>'))
    }
    for (let i of ll){usage.push(`<li>${i}</li>`)}
    pastholder.append(`
    <div class="tab">
        <input hidden type="checkbox" id="past${v.s}">
        <label class="tab-label" for="past${v.s}">${v.s}</label>
        <div class="tab-content">
            ${usage.join('<br>')}
        </div>
    </div>
    `)
    
})
future.map((v, i)=>{
    usage=[]
    ll=[]
    for (let i of v.u) {
        ll.push(i.join(': <br>'))
    }
    for (let i of ll){usage.push(`<li>${i}</li>`)}
    futureholder.append(`
    <div class="tab">
        <input hidden type="checkbox" id="future${v.s}">
        <label class="tab-label" for="future${v.s}">${v.s}</label>
        <div class="tab-content">
            ${usage.join('<br>')}
        </div>
    </div>
    `)
    
})