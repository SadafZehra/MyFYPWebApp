import React,{useState, useEffect} from 'react';


export default function Test(){
    let [res,setResult]=useState("")
    useEffect(()=>{
        fetch("/members").then((response)=>{
            return response.json()
        })
        .then((res)=>{
            console.log(res,"results from members")
        })

    },[])
    return(
        <>
        <h3>Image Classifcation</h3>
        <p>Api Testing</p>
        </>
    )
}