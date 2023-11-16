from django.shortcuts import render, redirect
from account.models import CustomUser
from .form import CreateStatement
from .models import Statement
# Create your views here.


def main(request):
    return render(request, 'site/main.html')


def statements(request):
    if request.user.is_staff and request.user.is_superuser:
        return redirect('admin_int')
    if request.user.is_anonymous == True:
        return redirect('/')
    user = request.user
    st_list = Statement.objects.filter(user=user)

    data = {
        'st_list': st_list
    }
    return render(request, 'site/statements.html', data)


def create_st(request):
    user = request.user
    if request.method == 'POST':
        form = CreateStatement(request.POST)
        if form.is_valid():
            s_form = form.save(commit=False)
            s_form.user = user
            s_form.save()
            return redirect('statements')
    form = CreateStatement
    data = {'form': form}
    return render(request, 'site/create_st.html', data)


def profile(request):

    return render(request, 'site/profile.html')


def admin_int(request):
    if request.user.is_staff and request.user.is_superuser:
        st_list = Statement.objects.all()
        data = {
            'st_list': st_list
        }
        return render(request, 'admin/statements_l.html', data)


def st_detail(request, pk):
    st_obj = Statement.objects.get(pk=pk)

    data = {
        'st_obj': st_obj
    }

    return render(request, 'admin/detail.html', data)


def accept_decline_st(request, operation, pk):
    if operation == 'accept':
        st = Statement.objects.get(pk=pk)
        st.status = 'Accepted'
        st.save()
    elif operation == 'decline':
        st = Statement.objects.get(pk=pk)
        st.status = 'Decline'
        st.save()
    return redirect('st_detail', pk)
