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

        private List<SentenceStructure> BindToModelList(string strJSONResult)
        {
            var result = JObject.Parse(strJSONResult);
            var listContent = new List<SentenceStructure>();
            if (result["values"].ToString() != "")
            {
                for (var i = 0; i < result["values"].ToArray().Length; i++)
                {
                    var text = result["values"][i]["text"].ToString().Split(' ');


                    listContent.Add(new SentenceStructure()
                    {
                        Sentence = result["values"][i]["text"].ToString(),
                    });
                    listContent[i].TextStructureParis = new List<TextStructure>();
                    var prePOSForm = "";
                    for (var j = 0; j < text.Length; j++)
                    {
                        var key = text[j];
                        var value = result["values"][i][key] == null ? "" : result["values"][i][key].ToString();
                        if (value != "")
                        {
                            var POSForm = "";
                            if (value.Substring(0, 1) == "N") { POSForm = "noun"; }
                            else if (value.Substring(0, 1) == "V") { POSForm = "verb"; }
                            else { POSForm = value; }
                            if (prePOSForm == POSForm)
                            {
                                listContent[i].TextStructureParis[listContent[i].TextStructureParis.Count - 1].TextKey += " " + key;
                            }
                            else
                            {
                                listContent[i].TextStructureParis.Add(new TextStructure()
                                {
                                    TextKey = key,
                                    TextValue = POSForm
                                });
                            }
                            prePOSForm = POSForm;
                        }
                    }
                }
            }
            return listContent;
        }

        private string GetPOSTaggedData()
        {
            string content = "";
            var fileStream = new FileStream(outputPOSTaggedJSON, FileMode.Open, FileAccess.Read);

            using (var streamReader = new StreamReader(fileStream, Encoding.UTF8))
            {
                content = streamReader.ReadToEnd();
            }

            return content;
        }

        private void ProcessTagData()
        {
            // 1) Create Process info
            string error = "", results = "";
            var psi = new ProcessStartInfo();
            psi.FileName = pythonExePath;

            // 2) Provide script and arguments
            psi.Arguments = outputPOSTaggedScriptFile;
            
            // 4)Execute process and get output
            using (var process = Process.Start(psi))
            {
                //error = process.StandardError.ReadToEnd();
                //results = process.StandardOutput.ReadToEnd();
            }

            //System.IO.File.WriteAllText(outputPOSTaggedJSON, results);
        }

    }
}