const adverbs=[
    {
        t:'When',
        m:'at that time',
        ex:[
            "When I arrived, he was talking on the phone => he was talking on the phone, at that time, I arrived.",
            "I visited the museum when I was  in Chicago."
        ],
        tenses:[
            ["[past s. / past simple continous]", "Depends"]
        ]
    },
    {
        t:'While/as',
        m:'during that time',
        ex:[
            "While I was walking home, it began to rain. => it began to rain, during that time, I was walking home",
            "As I was walking home, it began to rain."
        ],
        tenses:[
            ["past continious ", "D"]
        ]
    },
    {
        t:'By the time',
        m:'one event completed before anoyher',
        ex:[
            "By the time he arrived, we had already left. => We had already left then he arrived.",
            "By the time he comes, we will have already left."
        ],
        tenses:[
            ["present", "future perfect"],
            ["past", "past perfecr"]
        ]
    },
    {
        t:'Since',
        m:'from that time to the present',
        ex:[
            "I haven't seen him since he left this morning.",
            "I have known her since I was a child."
        ],
        tenses:[
            ["past", "present perfect"]
        ]
    },
    {
        t:'As soon as / once',
        m:'when an event happens, another event happens soon afterward',
        ex:[
            "[Once/as soon] as it stops raining, we willl leave."
        ],
        tenses:[
            ["present", "future"],
            ["[past, past perfect]", "past"]
        ]
    },
    {
        t:'As long as / So long as',
        m:'during all that time',
        ex:[
            "I will never speak to him again [as/so] long as I live."
        ],
        tenses:[
            ["present", "future"]
        ]
    },
    {
        t:'Untill/till',
        m:'to that time and then no longer',
        ex:[
            "We steyed there [untill/till] we finished our work."
        ],
        tenses:[
            ["past", "past"],
            ["present", "future"]
        ]
    },
    {
        t:'Whenever',
        m:'Everytime',
        ex:[
            "Wehenenevr I see her, I say hello."
        ],
        tenses:[
            ["present", "present"]
        ]
    },
    
]
const holder=$('.here')

adverbs.map((ad)=>{
    let tar=[]
    let tense=[]
    for (let i of ad.ex){tar.push(`<li>${i}</li>`)}
    for (let i of ad.tenses) {
        ll=[]
        for (let j of i){
            ll.push(`<td>${j}</td>`)
        }
        tense.push(`<tr>${ll.join('')}</tr>`)
    }
    holder.append(
        `
        <div class="tab">
            <input hidden type="checkbox" id="${ad.t}">
            <label class="tab-label" for="${ad.t}">${ad.t}</label>
            <div class="tab-content">
                    means: ${ad.m}
                    <br><br>
                    <ul>${tar.join('')}</ul>
                    <table class="table table-bordered border-primary">
                    <thead>
                        <tr>
                        <th scope="col">Time clause</th>
                        <th scope="col">Main clause</th>
                        </tr>
                    </thead>
                    <tbody>
                        ${tense.join('')}
                    </table>
                
            </div>
        </div>
        `
    )
})