use college_nosql

db.feedback.insertMany([
{
student_id:1,
course_code:"CS101",
semester:"2022-ODD",
rating:5,
comments:"Excellent",
tags:["challenging","well-structured"],
attachments:[{filename:"notes.pdf",size_kb:240}]
},
{
student_id:2,
course_code:"CS101",
semester:"2022-ODD",
rating:4,
comments:"Good",
tags:["challenging"]
},
{
student_id:3,
course_code:"CS102",
semester:"2022-ODD",
rating:3,
comments:"Average",
tags:["database"]
}
])

db.feedback.find({rating:5})

db.feedback.find({
course_code:"CS101",
tags:"challenging"
})

db.feedback.updateMany(
{rating:{$lt:3}},
{$set:{needs_review:true}}
)

db.feedback.deleteMany({
semester:"2021-EVEN"
})

db.feedback.aggregate([
{$match:{semester:"2022-ODD"}},
{
$group:{
_id:"$course_code",
avg_rating:{$avg:"$rating"},
feedback_count:{$sum:1}
}
},
{$sort:{avg_rating:-1}}
])

db.feedback.createIndex({
course_code:1
})
