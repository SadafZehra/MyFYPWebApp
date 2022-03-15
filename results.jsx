// import React,{useState,useEffect} from 'react'
// import { storage } from './Firebase/firebase'
// import Arrow from './Ui/arrow.png';
// import LineChart from './chart'

// export default function Results (){
//      async function getImage(){
//         //  await firebase
//      }

//     useEffect(() => {
//         fetch('/members').then((response) => {
//             if (response.ok) {
//                 return response.json()
//             }
//         })
//             .then((data) => {
//                 console.log(data,"data")
//             })
//     }, [])
//     return<>
//     <div className="container">
//                     <div className="heading">
//                         <h1>Results From Model</h1>
//                         </div>
//                     <div className="visualization">
//                         <div className="imageHolder">
//                             <div className="inputimage"></div>
//                             <div className="segmentedimage"></div>


//                         </div>

//                         <div className="modelbox">
//                             <div className="boxmod">
//                                 <h4>Machine Learning Image</h4>
//                                 <div className="blackbox">Ml Model</div>
//                                 <img src={Arrow} width='30px' height='30px' />
//                             </div>
//                         </div>
//                         <div className="modelresult">
//                             <h4>Results waiting........</h4>
//                             <LineChart />

//                         </div>
//                     </div>
//         </div>
//     </>
// }


import React,{useState,useEffect} from 'react'
import { storage } from './Firebase/firebase'
import Arrow from './Ui/arrow.png';
import LineChart from './chart'
import firebase from './Firebase/index'
import { getStorage, ref, getDownloadURL } from "firebase/storage";
import globe from './Ui/1.png'
import xrt from './Ui/xrt.png'

export default function Results (){
    const [imgobj,setimgobj]=useState({})
    const [imgurl,setImgurl]=useState()
    const [inpurl,setInpurl]=useState()
    const [data,setData]=useState({})
     async function getImage(){
        //  await firebase
     }

    useEffect(() => {
        fetch('/members').then((response) => {
            if (response.ok) {
                return response.json()
            }
        })
            .then((data) => {
                console.log(data,"data")
                setData(data)
            })
        
        
    }, [])
    useEffect(()=>{
        if(Object.keys(data).length){
            
            firebase.database().ref('/').child('images_frommodel').on('child_added',(s)=>{
                // console.log(s.key,'key')
                // console.log(s.val(),"inside map")
                let readtr=s.val()
                if (readtr['read']==true){
                      setimgobj({
                          key:s.key,
                          image:readtr['image'],
                          read:readtr['read']
                      })
                }
                  })

        }
        else{
            console.log("in us2 else",Object.keys(data).length)
        
            }

    },[data])
    useEffect(()=>{
        console.log("in us1 else",Object.keys(imgobj).length)
                console.log("imgobj2",imgobj)
                console.log(imgobj.image,"imagename")
                if(Object.keys(imgobj).length){
                    // pass
                    const storage = getStorage();
                    getDownloadURL(ref(storage, `images_frommodel/${imgobj.image}`))
                    .then((url) => {
                        // console.log(url,"url")
                        setImgurl(url)
                    })
                    .catch((e)=>{
                               console.log(e,"error")
                    })
                    // input image
                    getDownloadURL(ref(storage, `images_formodel/${imgobj.image}`))
                    .then((url) => {
                        console.log(url,"inpurl")
                        setInpurl(url)
                    })
                    .catch((e)=>{
                               console.log(e,"error")
                    })
                    // read true of the image
                    firebase.database().ref('/').child(`images_frommodel/${imgobj.key}`).set(
                        {
                            "image":imgobj.image,
                            "read":true
                        }
                    )

                }
                else{
              
                }
    },[imgobj])
    return<>
    {Object.keys(data).length ?<div className="containerresult">
                    <div className="heading">
                        <h1>Results From Model</h1>
                        <div className="modelresult">
                            <h2>Severity: {data.Severity}</h2>
                        </div>
                        </div>
                    <div className="visualization">
                        
                        <div className="imageHolder">
                            <div className="inputimage">
                                <h4>Input image</h4>
                                {inpurl?
                                <div className="imgcont1">
                                <img src={inpurl} className="imgcont" width='250px' height='250px'/></div>:
                                <div className="imgcont1">
                                <img src={xrt} width='250px'className="imgcont" height='250px'/></div>
                                }
                                
                            </div>
                            <div className="segmentedimage">
                            <h4>Segmented image</h4>
                            {imgurl?
                                <div className="imgcont1">

                            <img src={imgurl}  className="imgcont" width='250px' height='250px'/></div>:
                                <div className="imgcont1">
                                <img src={xrt}  className="imgcont" width='250px' height='250px'/></div>
}
                            </div>


                        </div>

                        <div className="modelbox">
                            <div className="boxmod">
                                <h4>Machine Learning Model</h4>
                                <div className="blackbox">Ml Model</div>
                            </div>
                        </div>
                        <br /><br /><br />
                        <h2>Histogram</h2>
                        <div className="chartresult">
                            
                            <LineChart data={data.Histogram}/>

                        </div>
                    </div>
        </div> :
        <><div className="containerresult">
            <h1>Results from Model</h1>
            <h3>Model Processing the calculation Please wait</h3>
            <br /><br /><br /><br /><br />
            <img src={globe} className='globe' />
        </div>
        </>}
    
    </>
}