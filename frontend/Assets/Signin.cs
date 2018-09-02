using UnityEngine;
using UnityEngine.UI;
using System.Collections;
using System.Collections.Generic;


public class Signin : MonoBehaviour
{
    private string url = "http://132.232.124.15:2333/signin/";

    // Use this for initialization
    void Start()
    {

    }

    // Update is called once per frame
    void Update()
    {

    }

    IEnumerator SendPost(string _url, WWWForm _wForm)
    {
        WWW postData = new WWW(_url, _wForm);
        yield return postData;
        if (postData.error != null)
        {
            Debug.Log(postData.error);
        }
        else
        {
            Debug.Log(postData.text);
        }
    }


    public void Click()
    {
        string nickname = GameObject.Find("Canvas/nickname/Text").GetComponent<Text>().text;
        string password = GameObject.Find("Canvas/password/Text").GetComponent<Text>().text;
        WWWForm form = new WWWForm();
        form.AddField("nickname", nickname);
        form.AddField("password", password);
        StartCoroutine(SendPost(url, form));
        Debug.Log(nickname);
        Debug.Log(password);
    }
}