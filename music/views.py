from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView,UpdateView, DetailView
from django.views import View
from accounts.models import User


from .models import Teacher,DirectMessage
from .forms import TeacherForm, DirectMessageForm #TODO: DirectMessageFormをimportしておく。


def logout_view(request):
    logout(request)
    return redirect('music:index')

class ListMusicView(ListView):
    template_name = 'music_list.html'
    model = Teacher
    #model = music 



class DetailMusicView(View):
    def get(self, request, pk, *args, **kwargs):

        context = {}

        teacher             = Teacher.objects.filter(id=pk).first()
        context["teacher"]  = teacher

        #TODO:編集用のフォームを作る
        context["form"]     = TeacherForm(instance=context["teacher"])

        # 自分が送ったメッセージと自分宛のメッセージをすべて表示


        # TODO:先生が自分に送られたメッセージを見る場合。
        if request.user.is_musician:
            context["sender_messages"]      = DirectMessage.objects.filter( sender=request.user.id )
            context["receiver_messages"]    = DirectMessage.objects.filter( receiver=request.user.id )

        # TODO:生徒が先生の詳細ページを見る場合
        else:
            # 複数の条件に合致するデータを取得したい場合、 ,で区切る。(AND検索)
            # アクセスしてきた生徒(request.user.id)が、このページの先生(pkを元に取得したteacher)に対して送ったメッセージを表示
            context["sender_messages"]      = DirectMessage.objects.filter( sender=request.user.id, receiver=teacher.user_id )

            # このページの先生(pkを元に取得したteacher)が、アクセスしてきた生徒(request.user.id)に対して送ったメッセージを表示
            context["receiver_messages"]    = DirectMessage.objects.filter( sender=teacher.user_id, receiver=request.user.id )


        # 生徒のプルダウンメニューを作る
        # 生徒のユーザーモデルを取り出す。
        context["students"]             = User.objects.filter(is_musician=False)


        return render(request,"music/music_detail.html" ,context)

    # このpkはTeacherのid。 Userのidではない
    def post(self, request, pk, *args, **kwargs):
    
        #TODO:ここでダイレクトメッセージの保存処理を書いていく。

        # request.POSTの中にmessageがある (先生が送る場合 receiverに生徒のUser.idが記録されている)
        copied              = request.POST.copy()

        # 送信( from_user )
        copied["sender"]    = request.user.id 


        #生徒→先生の場合、receiverを指定する
        if not request.user.is_musician:
            # 一旦Teacherを特定する。teacherからUserのidを取り出して記録する
            teacher             = Teacher.objects.filter(id=pk).first()

            # 宛先( to_user )
            copied["receiver"]  = teacher.user_id


        #先生→生徒の場合、テンプレートから送信先の生徒を選ぶ。




        # これでsender message receiverの3つが揃ったので、バリデーションして保存する。
        form    = DirectMessageForm(copied)
        
        # sender message receiverの3つ の値が正常であれば form.is_valid()はTrue
        if form.is_valid():
            print("バリデーションOK")

            # DBにデータを保存する
            form.save()


        """
        teacher             = Teacher.objects.filter(id=pk).first()
        copied["receiver"]  = teacher.user_id

        # 書き換えたデータをバリデーションする。
        form    = DirectMessageForm(copied)
        
        if form.is_valid():
            print("バリデーションOK")
            form.save()

        """
        return redirect("music:detail-music", pk)    

class DetailStudentView(View):

    # このpkはUserモデルのid
    def get(self, request, pk, *args, **kwargs):

        #ここでrequest.user.is_teacherがfalseの場合に限り表示させる。
        #↑ request.userはリクエストを送信したユーザー自身の情報になる。pkが閲覧対象のユーザーのidなので、pkを使ってUserモデルからデータを取り出す。

        user    = User.objects.filter(id=pk).first()

        #存在しない場合リダイレクト
        if not user:
            return redirect("")


        #講師である場合もリダイレクト
        if user.is_musician:
            return redirect("")

        context = {"user":user}

        #生徒である場合レンダリング
        return render(request, "music/student_detail.html", context )



#生徒の個別ページを作りたい

#class DetailStudentView(View):
#    def get(self,request,pk,*args,**kwargs):
        #ここでrequest.user.is_teacherがfalseの場合に限り表示させる。


# #不具合のあるVeiw
# #class CreateMusicView(CreateView):    
#    template_name = 'music/music_create.html'
#    model = Teacher
    
#    fields = ("movie","fee","academic","experience","certificate","reputation","message","oneword","lang","teaching_inst","year","revel","pic","user_id")
#    success_url = '/music/'

#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context['user_id'] = " User.objects.get()pk =self .kwargs['int:pk']"
#        return context

class CreateMusicView(CreateView):    
    template_name = 'music/music_create.html'
    model = Teacher
    #fields = ("movie","fee","academic","experience","certificate","reputation","message","oneword","lang","teaching_inst","year","revel","pic","user_id")
    fields = ("fee","academic","experience","certificate","reputation","message","oneword","lang","teaching_inst","year","revel")

    def form_valid(self, form):
        object = form.save(commit=False)
        object.user_id = self.request.user
    
        object.save()

        return super().form_valid(form)

    success_url = '/music/'


    

#class CreatePeopleView(CreateView):    
#    template_name = 'music/music_people_create.html'
#    model = User
#    fields = ("first_name","last_name","","city","introduction")

#    success_url = '/music/'


#class DeleteMusicView(View):
    #template_name = 'music/music_confirm_delete.html'
    #model = Teacher
    #success_url = '/music/'

    

class DeleteMusicView(View):
    
    def get(self, request, pk, *args, **kwargs):
        teacher = Teacher.objects.filter(id=pk).first()

        #teacherの存在確認(存在しない場合はリダイレクト)
        if not teacher:
            return  redirect("music:index")

        #ここで存在しないteacherの.user_idを参照するとエラーになる
        if teacher.user_id == request.user:

            #TODO:ここで削除対象のUserモデルのデータを特定する。その上で.delete()を実行する。
            user    = User.objects.filter(id=request.user.id).first()
            user.delete()

        # トップページへリダイレクト
        return redirect("music:index")
 



# ここがトップページ( http://127.0.0.1:8000/ )にアクセスした時実行される
def index_view(request):

    #TODO: 未ログインユーザーの場合、ログインページへリダイレクトするように仕立てる
    # .is_authenticated属性を参照し、未ログインであればFalseが帰ってくる
    if not request.user.is_authenticated:
        return redirect("accounts:login")

    #ここで先生かどうかを判定する。未ログイン状態ではis_musicianは参照できない。
    if request.user.is_musician:
        #TODO:ここにDetailMusicViewSecondのnameを書く
        teacher = Teacher.objects.filter(user_id=request.user.id).first()
        return redirect("music:detail-music" , teacher.id )

    #アクセスした人が先生ではない場合、先生の一覧を表示する

    object_list = Teacher.objects.all()
    return render(request, 'music/index.html',{'object_list': object_list})


class UpdateMusicView(UpdateView): 
    model = Teacher
    fields = ("movie","fee","academic","experience","certificate","reputation","message","oneword","lang","year","revel","pic","user_id")
    template_name = 'music/music_update.html'
    success_url = '/music/' 

    ## DetailMusicView から直接 編集処理をしたい場合は POSTを
    ## DetailMusicView から UpdateMusicViewへ移動して編集処理をしたい場合は、GETを

    #TODO:現状、自分以外のユーザーも編集ができてしまう。
    #対策1: UpdateViewではなくViewを継承してpostメソッドを作る。
    #対策2: pkを元にTeacherで検索。teacher.user_id と request.user が一致していれば編集許可
    # 削除の前にやった処理と同じ



class MypageView(View):
    def get(self, request, *args, **kwargs):

        print(request.user.id)

        context = {}
        context["teacher"] = Teacher.objects.filter(user_id=request.user.id).first()

        return render(request, "music/mypage.html",context)

    def post(self, request, *args, **kwargs):

        return redirect("mypage") 

## ダイレクトメッセージのみ実装

class UserView(View):
    def get(self, request, pk, *args, **kwargs):


        return render(request, "")

    def post(self, request, pk, *args, **kwargs):
        ## TODO: ここでユーザーに対して

        return redirect("")

