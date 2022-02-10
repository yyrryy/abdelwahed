courses = [
  "Writings Paragraph",
  "Spoken English",
  "Study Skills",
  "Grammar 1",
  "Guided Reading",
  "Langues I ANG",
  "Reading Compr Précis 1",
  "Reading Compr Précis 2",
  "Grammar 2",
  "Readings in Culture",
  "Langues II",
  "Composition 1",
  "Oral communication",
  "Business Communication",
];

links = [
  "./writing",
  "./spoken",
  "./study",
  "./grammar1",
  "./guided",
  "./lang1",
  "./reading1",
  "./reading2",
  "./grammar2",
  "./culture",
  "./lang2",
  "./comp1",
  "./comunication",
  "./business",
];


$('.goto').attr('href', links[0])
courses.map((v, i) => {
  $(".gotoselect").append(`<option value=${links[i]}>${v}</option>`);
});

$('.gotoselect').on('change', (e) => {
  v = e.target.value
  $('.goto').attr('href', v)
})