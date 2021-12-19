const exercices=[
    {
        q:"_______________________ the latest news? – The president ______________________ that he _____________________ to resign next summer. – That's not new. I _____________________  that for ages!",
        ch:["YOU HEAR", "JUST ANNOUCE", "PLAN", "KNOW"],
        a:"Have you heard the latest news? – The president has just announced that he is planning to resign next summer. – That's not new. I have known that for ages!",
        h:['Have you heard', 'as just announced', 'is planning', 'have known'],
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
        ch:["BE", "BE ABLE TO)"],
        a:"He have been in hospital for a few days and the doctor said he whould be able to come home on Monday",
        h:['have been', 'whould be able to'],
        e:['expl for have been', 'zxpl for would']
    },
    {
        q:"He _____________________ in hospital for a few days and the doctor said he _____________________ come home on Monday.",
        ch:["BE", "BE ABLE TO)"],
        a:"He have been in hospital for a few days and the doctor said he whould be able to come home on Monday",
        h:['have been', 'whould be able to'],
        e:['expl for have been', 'zxpl for would']
    },
    {
        q:"He _____________________ in hospital for a few days and the doctor said he _____________________ come home on Monday.",
        ch:["BE", "BE ABLE TO)"],
        a:"He have been in hospital for a few days and the doctor said he whould be able to come home on Monday",
        h:['have been', 'whould be able to'],
        e:['expl for have been', 'zxpl for would']
    },
    {
        q:"He _____________________ in hospital for a few days and the doctor said he _____________________ come home on Monday.",
        ch:["BE", "BE ABLE TO)"],
        a:"He have been in hospital for a few days and the doctor said he whould be able to come home on Monday",
        h:['have been', 'whould be able to'],
        e:['expl for have been', 'zxpl for would']
    },
    {
        q:"He _____________________ in hospital for a few days and the doctor said he _____________________ come home on Monday.",
        ch:["BE", "BE ABLE TO)"],
        a:"He have been in hospital for a few days and the doctor said he whould be able to come home on Monday",
        h:['have been', 'whould be able to'],
        e:['expl for have been', 'zxpl for would']
    },
    {
        q:"He _____________________ in hospital for a few days and the doctor said he _____________________ come home on Monday.",
        ch:["BE", "BE ABLE TO)"],
        a:"He have been in hospital for a few days and the doctor said he whould be able to come home on Monday",
        h:['have been', 'whould be able to'],
        e:['expl for have been', 'zxpl for would']
    },
    {
        q:"He _____________________ in hospital for a few days and the doctor said he _____________________ come home on Monday.",
        ch:["BE", "BE ABLE TO)"],
        a:"He have been in hospital for a few days and the doctor said he whould be able to come home on Monday",
        h:['have been', 'whould be able to'],
        e:['expl for have been', 'zxpl for would']
    },
    {
        q:"He _____________________ in hospital for a few days and the doctor said he _____________________ come home on Monday.",
        ch:["BE", "BE ABLE TO)"],
        a:"He have been in hospital for a few days and the doctor said he whould be able to come home on Monday",
        h:['have been', 'whould be able to'],
        e:['expl for have been', 'zxpl for would']
    },
    {
        q:"He _____________________ in hospital for a few days and the doctor said he _____________________ come home on Monday.",
        ch:["BE", "BE ABLE TO)"],
        a:"He have been in hospital for a few days and the doctor said he whould be able to come home on Monday",
        h:['have been', 'whould be able to'],
        e:['expl for have been', 'zxpl for would']
    },
    {
        q:"He _____________________ in hospital for a few days and the doctor said he _____________________ come home on Monday.",
        ch:["BE", "BE ABLE TO)"],
        a:"He have been in hospital for a few days and the doctor said he whould be able to come home on Monday",
        h:['have been', 'whould be able to'],
        e:['expl for have been', 'zxpl for would']
    },
    {
        q:"He _____________________ in hospital for a few days and the doctor said he _____________________ come home on Monday.",
        ch:["BE", "BE ABLE TO)"],
        a:"He have been in hospital for a few days and the doctor said he whould be able to come home on Monday",
        h:['have been', 'whould be able to'],
        e:['expl for have been', 'zxpl for would']
    },
    {
        q:"He _____________________ in hospital for a few days and the doctor said he _____________________ come home on Monday.",
        ch:["BE", "BE ABLE TO)"],
        a:"He have been in hospital for a few days and the doctor said he whould be able to come home on Monday",
        h:['have been', 'whould be able to'],
        e:['expl for have been', 'zxpl for would']
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
            ${i+1}. ${ex.q}
            <div class="text-primary">
                (${ex.ch.join(', ')})
            </div>
           <div class="tabs">
                <div class="tab mb-5">
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