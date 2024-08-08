from django.shortcuts import render
from .models import BitsByBits
from .forms import BitsByBitsForm
from django.shortcuts import get_object_or_404, redirect
# Create your views here.
def index(request):
    return render (request, 'index.html')

def tweet_list(request):
    tweets = BitsByBits.objects.all().order_by('-created_at')
    return render(request, 'tweet_list.html', {'tweets': tweets})

def tweet_create(request):
    if request.method == "POST":
        form = BitsByBitsForm(request.POST, request.FILES)
        if form.is_valid():
            tweet= form.save(commit=False)
            tweet.user= request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = BitsByBitsForm()
    return render(request, 'tweet_form.html', {'form': form})


def tweet_edit(request, tweet_id):
    tweet= get_object_or_404(BitsByBits, pk=tweet_id, user=request.user)
    if request.method=='POST':
        form = BitsByBitsForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet= form.save(commit=False)
            tweet.user= request.user
            tweet.save()
            return redirect('tweet_list')

    else: 
        form= BitsByBitsForm(instance=tweet)
        return render(request, 'tweet_form.html', {'form': form})
    
def tweet_delete(request, tweet_id):
    tweet= get_object_or_404(BitsByBits, pk= tweet_id, user= request.user)
    if request.method=='POST':
        tweet.delete()
        return redirect('tweet_list')
    return render(request, 'tweet_confirm_delete.html', {'tweet': tweet})