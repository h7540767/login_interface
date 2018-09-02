using UnityEngine;
using System.Collections;

public class Login : MonoBehaviour
{

    private string nickname;//用户名
    private string password;//密码
    private string info;//信息

    void Start()
    {
        //初始化
        nickname = "";
        password = "";
        info = "";
    }

    IEnumerator SendPost(string _url, WWWForm _wForm)
    {
        WWW postData = new WWW(_url, _wForm);
        yield return postData;
        if (postData.error != null)
        {
            info = postData.error;
        }
        else
        {
            info = postData.text;
        }
    }

    void OnGUI()
    {
        //用户名
        GUI.Label(new Rect(20, 20, 50, 20), "昵  称");
        nickname = GUI.TextField(new Rect(80, 20, 100, 20), nickname, 15);//15为最大字符串长度
                                                                          //密码
        GUI.Label(new Rect(20, 50, 50, 20), "密  码");
        password = GUI.PasswordField(new Rect(80, 50, 100, 20), password, '*');//'*'为密码遮罩
                                                                                       //信息
        GUI.Label(new Rect(20, 100, 300, 20), info);
        //登录按钮
        if (GUI.Button(new Rect(80, 80, 40, 20), "登录"))
        {
            string url = "http://132.232.124.15:2333/signin/";
            WWWForm form = new WWWForm();
            form.AddField("nickname", nickname);
            form.AddField("password", password);
            StartCoroutine(SendPost(url,form));
        }

        if (GUI.Button(new Rect(140, 80, 40, 20), "注册"))
        {
            string url = "http://132.232.124.15:2333/signup/";
            WWWForm form = new WWWForm();
            form.AddField("nickname", nickname);
            form.AddField("password", password);
            StartCoroutine(SendPost(url, form));
        }
    }
}
