const adverbs=[
    {
        t:'When',
        m:'at that time',
        ex:[
            "When I arrived, he was talking on the phone => he was talking on the phone, at that time, I arrived.",
            "I visited the museum when I was  in Chicago."
        ]
    },
    {
        t:'While/as',
        m:'during that time',
        ex:[
            "While I was walking home, it began to rain. => it began to rain, during that time, I was walking home",

            "As I was walking home, it began to rain."
        ]
    },
    {
        t:'By the time',
        m:'one event completed before anoyher',
        ex:[
            "By the time he arrived, we had already left. => We had already left then he arrived.",
            "By the time he comes, we will have already left."
        ]
    },
    {
        t:'Since',
        m:'from that time to the present',
        ex:[
            "I haven't seen him since he left this morning.",
            "I have known her since I was a child."
        ]
    },
    
]
const holder=$('.here')

adverbs.map((ad)=>{
    let tar=[]
    for (let i of ad.ex){tar.push(`<li>${i}</li>`)}
    holder.append(
        `
        <div class="tab">
            <input hidden type="checkbox" id="${ad.t}">
            <label class="tab-label" for="${ad.t}">${ad.t}</label>
            <div class="tab-content">
                    ${ad.m} == ${ad.m}
                    <br>
                    <ul>${tar.join('<br>')}</ul>
                
            </div>
        </div>
        `
    )
})