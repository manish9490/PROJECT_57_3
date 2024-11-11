from django.shortcuts import render

def resume(request):
    context = {
        'name': 'Manish',
        'email': 'manishsaikatla@gmail.com',
        'phone': '7386346211',
        'education': [
            {
                'degree': 'B.Tech in AI & DS',
                'institution': 'KL University',
                
            },
            {
                'degree': 'Intermediate (MPC)',
                'institution': 'Intermediate School',
                
            },
            {
                'degree': 'SSC',
                'institution': 'High School',
               
            }
        ],
        'experience': [],
        'skills': ['HTML', 'CSS', 'Python', 'Java', 'JavaScript', 'Django'],
        'projects': [
            {
                'name': 'Live Stream App',
                'description': 'An application for streaming live content, using Django and WebSockets.',
                
            },
            {
                'name': 'E-commerce App',
                'description': 'An online shopping platform with payment integration.',
              
            }
        ],
        'certifications': [
            {
                'title': 'Certified Python Developer',
                'issuing_org': 'Coursera',
                
            },
            {
                'title': 'AWS Certified',
                'issuing_org': 'Amazon Web Services',
               
            }
        ],
        'hobbies': ['Reading', 'Traveling', 'Watching Movies'],
    }
    return render(request, 'App_52_3/resume.html', context)
