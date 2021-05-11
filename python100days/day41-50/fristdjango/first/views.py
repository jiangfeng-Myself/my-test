from django.shortcuts import render
from random import sample
from django.http import HttpResponse

# Create your views here.
def show_index(request):
    return HttpResponse('<h1>Hello, Django</h1>')

def show_index2(request):
    fruits =[
        'Apple', 'Orange', 'Pitaya', 'Durian', 'Waxberry', 'Blueberry',
        'Grape', 'Peach', 'Pear', 'Banana', 'Watermelon', 'Mango'
    ]
    selected_fruits = sample(fruits, 3)
    content = '<h3>今天推荐的水果是：</h3>'
    content += '<hr>'
    content += '<ul>'
    for fruit in selected_fruits:
        content +=f'<li>{fruit}</li>'
    content += '</ul>'
    return HttpResponse(content)

def show_index3(request):
    fruits = [
        'Apple', 'Orange', 'Pitaya', 'Durian', 'Waxberry', 'Blueberry',
        'Grape', 'Peach', 'Pear', 'Banana', 'Watermelon', 'Mango'
    ]
    selected_fruits = sample(fruits, 3)
    return render(request, 'index.html', {'fruits': selected_fruits})
    # render函数的第一个参数是请求对象request, 第二个参数是我们要渲染的模板页的名称，第三个参数是要渲染到页面上的数据