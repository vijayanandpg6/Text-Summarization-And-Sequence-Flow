using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using System.IO;
using System.Text;
using WebApp.Models;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using System.Threading;

namespace WebApp.Controllers
{
    public class HomeController : Controller
    {
        static string baseFileName = "outFile4";
        string uploadFilePath = @"";
        string pythonExePath = @"..\Programs\Python\Python35\python.exe";
        string inputSummarizeFilePath = @"..\TextManipulationRepo\ProcessFiles\InputTextDocument.txt";
        string outputSummarizeFilePath = @"..\TextManipulationRepo\ProcessFiles\SummarizedTextDocument.txt";
        //string outputSummarizeFileName = "test.sample11.txt";
        string testSummarizeFile = @"..\Archive\TextSummarization\TensorFlow-Summarization-master\TensorFlow-Summarization-master\script\test.py";
        string testSummarizeFileNLTK = @"..\TextManipulationRepo\PythonScripts\nlpShorteningByText.py";
        string testSummarizeLinkFileNLTK = @"..\TextManipulationRepo\PythonScripts\nlpShorteningByLink.py";
        string outputPOSTaggedJSON = @"..\TextManipulationRepo\ProcessFiles\JSONSummarizedTextDocument.txt";
        string outputPOSTaggedScriptFile = @"..\TextManipulationRepo\PythonScripts\convertToPOSjson.py";
        // GET: Home
        public ActionResult Index()
        {
            //WSDDisplay();
            return View();
        }

        [HttpPost]
        public ActionResult WSDDisplay(InputTxt inputTxt)
        {
            string posTaggedData = "", summarizedText = "", mainInputText = "", mainInputLinkText = "";
            var filePath = inputSummarizeFilePath;
            if(inputTxt.InputUploadValue != null && inputTxt.InputUploadValue != string.Empty){
                
            }
            else if(inputTxt.InputTextValue != null && inputTxt.InputTextValue != string.Empty)
            {
                mainInputText = inputTxt.InputTextValue;
            }
            else if(inputTxt.InputLinkValue != null && inputTxt.InputLinkValue != string.Empty)
            {
                mainInputLinkText = inputTxt.InputLinkValue;
            }

            

            if(inputTxt.InputLinkValue != null && inputTxt.InputLinkValue != string.Empty)
            {
            
            }
            else
            {
            
            }

            //summarizedText = GetSummarizedText();

            //ProcessTagData();

            Thread.Sleep(5000);
            

            return View(listContent);
        }
        
    }
}